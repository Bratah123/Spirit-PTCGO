from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da38bf32-8fcf-54c2-926d-99bb2cc8ee4b",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Heavy Pincers",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Claw Rend",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)