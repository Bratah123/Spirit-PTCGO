from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e741793-cbf8-50c9-9947-4d303a67c51d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Single Strike", "Beedrill"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=3,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Persist Sting",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached, it is Knocked Out.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Jet Spear",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=110,
            effect=unimplemented,
        ),
    ],
)