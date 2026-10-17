from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc3455ac-0d54-53c5-855f-2fb0ea4327df",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name",
    display_name="Krookodile",
    searchable_by=["Krookodile", "Stage 2", "Krookodile"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Torment",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Krookoroll",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)