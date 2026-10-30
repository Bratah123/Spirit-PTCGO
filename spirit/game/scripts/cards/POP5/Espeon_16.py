from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import purple_ray_confuse_actives, psychic_boom


card = PokemonCardDef(
    guid="acd30c7d-b060-5081-81ad-cc053b03bd59",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon ★",
    searchable_by=["Espeon \u2605", "Basic", "Star", "Espeon"],
    subtypes=["Basic", "Star"],
    collector_number=16,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Ability(
            title="Purple Ray",
            game_text="Once during your turn, when you put Espeon Star from your hand onto your Bench, you may use this power. Each Active Pokémon (both yours and your opponent's) is now Confused.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=purple_ray_confuse_actives(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Psychic Boom",
            game_text="Does 30 damage plus 10 more damage for each Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=psychic_boom(30, 10),
        ),
    ],
)
