from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import poison_bite, spider_web


card = PokemonCardDef(
    guid="e3339b7a-a22b-5bdf-a091-089125437f2f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Spider Web",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't retreat. (Benching or evolving that Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.GRASS: 1},
            effect=spider_web,
        ),
        Attack(
            title="Poison Bite",
            game_text="If this attack damages the Defending Pok\u00e9mon, the Defending Pok\u00e9mon is now Poisoned and you remove a number of damage counters from Ariados equal to half that damage (rounded up to the nearest 10). If Ariados has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 3},
            damage=20,
            effect=poison_bite,
        ),
    ],
)
