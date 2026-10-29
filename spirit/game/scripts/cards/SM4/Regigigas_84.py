from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import bedrock_breaker
from spirit.game.card_effects.sm4 import SealOfAntiquityPassive


card = PokemonCardDef(
    guid="971f3507-0cac-50dd-85fb-5d9e8ce52ade",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Seal of Antiquity",
            game_text="This Pok\u00e9mon can't attack unless Regirock, Regice, and Registeel are on your Bench.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=SealOfAntiquityPassive(),
        ),
        Attack(
            title="Giant Stomp",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
            # STUB: attack effect not implemented
            effect=bedrock_breaker,
        ),
    ],
)