from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import lava_flow, magma_pool


card = PokemonCardDef(
    guid="bd687ca4-34f0-5b6e-b7d8-57234ae68ffe",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Magma Pool",
            game_text="If Magcargo is your Active Pok\u00e9mon and moves to the Bench, remove 1 Fire Energy card attached to Magcargo, if any, and attach it to the new Active Pok\u00e9mon. (You can't choose an Energy card that you used to pay the Retreat Cost.)",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_RETREAT,
            effect=magma_pool,
        ),
        Attack(
            title="Lava Flow",
            game_text="You may discard any number of Fire Energy cards attached to Magcargo when you use this attack. If you do, this attack does 40 damage plus 20 more damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=40,
            damage_operator="+",
            effect=lava_flow,
        ),
    ],
)
