from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import tentacle_wrap, unused_energy_bonus


card = PokemonCardDef(
    guid="e071eae8-6bb6-5409-b301-91312631ad71",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOctillery.Name",
    display_name="Dark Octillery",
    searchable_by=["Dark Octillery", "Stage 1", "DarkOctillery"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Ink Blast",
            game_text="This attack does 20 damage plus 10 more damage for each Energy attached to Dark Octillery but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20),
        ),
        Attack(
            title="Tentacle Wrap",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, during your opponent's next turn, your opponent pays Colorless more to retreat the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=tentacle_wrap,
        ),
    ],
)
