from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import detonate


card = PokemonCardDef(
    guid="8d6896fd-ca91-5b8a-a503-8130a76dd5bd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGraveler.Name",
    display_name="Brock's Graveler",
    searchable_by=["Brock's Graveler", "Stage 1", "BrocksGraveler"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Detonate",
            game_text="Does 10 damage to each Pok\u00e9mon on each player's bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Brock's Graveler does 50 damage to itself. If there is a Stadium card in play, discard it.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
            effect=detonate,
        ),
    ],
)
