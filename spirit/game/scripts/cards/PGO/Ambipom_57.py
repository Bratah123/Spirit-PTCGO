from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="822d008a-f144-56e1-ae7e-3779ccfd515c",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="PGO",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Ability(
            title="Primate Dexterity",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            effect=unimplemented,
        ),
        Attack(
            title="Full Tilt Fling",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)