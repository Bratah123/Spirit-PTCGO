from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="97458fa2-333e-5a2d-89dc-74eb11979644",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    display_name="Swadloon",
    searchable_by=["Swadloon", "Stage 1", "Swadloon"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="String Shot",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
