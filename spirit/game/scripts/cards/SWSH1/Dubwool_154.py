from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3fa38ce-33c2-5033-9ffb-07c430cf3a49",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dubwool.Name",
    display_name="Dubwool",
    searchable_by=["Dubwool", "Stage 1", "Dubwool"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooloo.Name",
    family_id=831,
    abilities=[
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)