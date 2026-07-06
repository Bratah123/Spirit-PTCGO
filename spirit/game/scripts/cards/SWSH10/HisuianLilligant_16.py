from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eba08eb0-65c6-5add-8c74-f63d942baddd",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianLilligant.Name",
    display_name="Hisuian Lilligant",
    searchable_by=["Hisuian Lilligant", "Stage 1", "HisuianLilligant"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Twister Lutz",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)