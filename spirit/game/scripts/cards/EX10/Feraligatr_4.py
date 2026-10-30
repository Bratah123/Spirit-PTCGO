"""STUB: effect not implemented — do not guess mechanics.
Feraligatr (EX10 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import intimidating_fang_passive, pull_away_to_4_hand, tonnage_optional_recoil

card = PokemonCardDef(
    guid="ff72bdfe-f699-5b05-aa28-3d0d06200cf2",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as Feraligatr is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 10 (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=intimidating_fang_passive(10),
        ),
        Attack(
            title="Pull Away",
            game_text="If your opponent has 5 of more cards in his or her hand, your opponent discards a number of cards until your opponent has 4 cards left in his or her hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=pull_away_to_4_hand(),
        ),
        Attack(
            title="Tonnage",
            game_text="You may do 50 damage plus 30 more damage. If you do, Feraligatr does 30 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=tonnage_optional_recoil(50, 30, 30),
        ),
    ],
)