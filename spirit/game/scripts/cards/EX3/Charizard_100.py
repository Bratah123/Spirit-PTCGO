"""STUB: effect not implemented — do not guess mechanics.
Charizard (EX3 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flip_attach_n_from_discard, may_discard_energy_then_snipe
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import energy_provides_type

card = PokemonCardDef(
    guid="cb6b707c-0aa9-5069-bb81-01822a57c8ab",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=100,
    set_code="EX3",
    rarity=Rarities.RareSecret,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Collect Fire",
            game_text="Flip a coin. If heads, search your discard pile for 2 Fire Energy cards and attach them to Charizard (1 if there is only 1).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=flip_attach_n_from_discard(2, predicate=lambda c: is_basic_energy_card(c) and energy_provides_type(c, PokemonTypes.FIRE.value)),
        ),
        Attack(
            title="Flame Pillar",
            game_text="You may discard a Fire Energy card attached to Charizard. If you do, choose 1 of your opponent's Benched Pok\u00e9mon and do 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=may_discard_energy_then_snipe(PokemonTypes.FIRE, 30),
        ),
    ],
)