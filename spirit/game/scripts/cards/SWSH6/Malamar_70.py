from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f0653d1-4ca3-514d-9e74-0e156861997d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Rapid Strike", "Malamar"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=70,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Rapid Strike Tentacles",
            game_text="Reveal any number of Rapid Strike cards from your hand. This attack does 40 damage for each card you revealed in this way. Then, shuffle those cards into your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)