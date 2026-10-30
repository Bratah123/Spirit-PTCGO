from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import leech_seed


card = PokemonCardDef(
    guid="c9d24fbc-8bca-5f9d-95af-1bb5c4adfafb",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2", "Jumpluff"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=187,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Leech Seed",
            game_text="If this attack damages the Defending Pok\u00e9mon (after applying Weakness and Resistance), remove 1 damage counter from Jumpluff, if it has any.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=leech_seed,
        ),
    ],
)
