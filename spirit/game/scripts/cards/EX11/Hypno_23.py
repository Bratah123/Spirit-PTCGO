"""STUB: effect not implemented — do not guess mechanics.
Hypno (EX11 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import binding_aura_passive, sleep_inducer


card = PokemonCardDef(
    guid="08af59cb-69f1-5e53-9ef5-754fb5240705",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Binding Aura",
            game_text="Your opponent can't play any Basic Pok\u00e9mon or Evolution cards from his or her hand to evolve an Active Pok\u00e9mon and can't attach any Energy cards from his or her hand to an Asleep Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=binding_aura_passive(),
            effect=None,
        ),
        Attack(
            title="Sleep Inducer",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=sleep_inducer(),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)