from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ba3070e-691a-5518-a425-76f34603cc99",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1", "Nuzleaf"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Surprise Punch",
            game_text="Move an Energy attached to the Defending Pok\u00e9mon to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)