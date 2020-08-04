import {
    LOAD_PRODUCTS, ADD_PRODUCT
} from './actionTypes'
import { DELETE_PRODUCT } from './products'

export function loadProducts(productList) {
    return {
        type: LOAD_PRODUCTS,
        productList
    }

}

export function addProduct(product){
    return{
        type:ADD_PRODUCT,
        product
    }
}

export function deleteProduct(product_id){
    return{
        type:DELETE_PRODUCT,
        product_id
    }
}