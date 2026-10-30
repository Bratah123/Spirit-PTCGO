"""STUB: effect not implemented — do not guess mechanics.
Exploud (EX5 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.card_effects.ex import bass_control, breaking_sound

card = PokemonCardDef(
    guid="27e04e9c-ed88-5b6c-9bde-55f5e1395b0f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name",
    display_name="Exploud",
    searchable_by=["Exploud", "Stage 2", "Exploud"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Breaking Sound",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=breaking_sound(10),
        ),
        Attack(
            title="Bass Control",
            game_text="Does 30 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bass_control(30),
        ),
        Attack(
            title="Thunderous Roar",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
        ),
    ],
)