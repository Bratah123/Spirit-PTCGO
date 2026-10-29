from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import attack_effect_shield_passive
from spirit.game.card_effects.sm6 import trinity_star, trinity_star_condition

card = PokemonCardDef(
    guid="c8c0e0eb-bab8-5d40-8644-2a2589e7cc35",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusPrismStar.Name",
    display_name="Arceus {*}",
    searchable_by=["Arceus {*}", "Basic", "Prism Star", "ArceusPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=96,
    set_code="SM6",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Ability(
            title="First Law",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Trinity Star",
            game_text="You can use this attack only if you have Grass, Water, and Lightning Pok\u00e9mon on your Bench. Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            condition=trinity_star_condition,
            effect=trinity_star,
        ),
    ],
)
