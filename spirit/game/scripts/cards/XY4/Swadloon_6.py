from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="8ef67423-35b8-5b18-ac07-5e6db4223ce8",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    display_name="Swadloon",
    searchable_by=["Swadloon", "Stage 1", "Swadloon"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="XY4",
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
            title="Protect",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)