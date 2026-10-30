"""EX12 Legend Maker — Furret.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.card_effects.ex import do_the_wave
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="6ab6e14d-86fe-5f1a-817f-99c8cc92eb2f",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Do the Wave",
            game_text="Does 10 damage plus 10 more for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=do_the_wave(10, 10),
        ),
    ],
)