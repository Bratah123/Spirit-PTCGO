from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4088b77-781f-50f0-93e7-4c8db08f5c7d",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragapult.Name",
    display_name="Dragapult",
    searchable_by=["Dragapult", "Stage 2", "Fusion Strike", "Dragapult"],
    subtypes=["Stage 2", "Fusion Strike"],
    collector_number=130,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Fusion Strike Assault",
            game_text="This attack does 30 damage for each of your Fusion Strike Pok\u00e9mon in play.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)