from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9bd76d12-74e3-5f5f-aafe-61ddb7dd2f52",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=69,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Dragonaxe",
            game_text="Does 40 damage times the amount of Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Strike of the Champion",
            game_text="If the Defending Pok\u00e9mon is a Team Plasma Pok\u00e9mon, it is Knocked Out. (If the Defending Pok\u00e9mon is not a Team Plasma Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
    ],
)