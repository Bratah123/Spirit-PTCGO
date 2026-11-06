from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack, gust_attack


card = PokemonCardDef(
    guid="735f9a8d-f737-5df3-b40a-d07efa0ff9fb",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    display_name="Cascoon",
    searchable_by=["Cascoon", "Stage 1", "Cascoon"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Tangle Drag",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=heal_attack(20),
        ),
    ],
)