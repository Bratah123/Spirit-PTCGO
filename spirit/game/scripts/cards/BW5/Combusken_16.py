from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ac4493bc-4f47-5025-b10e-0306ba295e25",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1", "Combusken"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Double Kick",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)