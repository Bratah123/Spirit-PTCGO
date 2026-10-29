from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm7 import (
    sol_shade_passive,
)


card = PokemonCardDef(
    guid="e1417564-6934-525e-9f7f-fda2e099096e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=337,
    abilities=[
        Ability(
            title="Sol Shade",
            game_text="If you have Solrock in play, Fire Pok\u00e9mon in play (both yours and your opponent's) have no Abilities, except Pok\u00e9mon-GX and Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=sol_shade_passive,
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)