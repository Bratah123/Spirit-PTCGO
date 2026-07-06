from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7384f801-e9f5-559f-92f5-2f16b740cb32",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=110,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=410,
    abilities=[
        Ability(
            title="Primal Fortress",
            game_text="Your Pok\u00e9mon take 30 less damage from attacks from your opponent's Pok\u00e9mon V (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Iron Tackle",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)