from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb9078f7-b5e5-5bc7-b8f5-f16ccc1f41d4",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=125,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Wing Flick",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Air Slash",
            game_text="Flip a coin. If tails, discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)