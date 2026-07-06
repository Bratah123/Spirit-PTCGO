from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e820b680-0fd1-5cbc-bcf2-f509b9950590",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1", "Sandaconda"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Ability(
            title="Sand Sac",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Power Press",
            game_text="If this Pok\u00e9mon has at least 1 extra Fighting Energy attached (in addition to this attack's cost), this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)