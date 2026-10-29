from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm3 import ThickFatPassive

card = PokemonCardDef(
    guid="578219dd-cc6d-58b2-ae32-acc4ec3ffab3",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="This Pok\u00e9mon takes 30 less damage from the attacks of your opponent's Fire or Water Pok\u00e9mon (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=ThickFatPassive(),
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
