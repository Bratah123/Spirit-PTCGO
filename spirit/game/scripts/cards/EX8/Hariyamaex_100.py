"""STUB: effect not implemented — do not guess mechanics.
Hariyama ex (EX8 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import commanding_aura_no_stadium, knock_off_random_hand, pivot_throw_takes_more


card = PokemonCardDef(
    guid="0c31ce9c-ab41-5988-8bad-e58fe4f82f5d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyamaex.Name",
    display_name="Hariyama ex",
    searchable_by=["Hariyama ex", "Stage 1", "ex", "Hariyamaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=100,
    set_code="EX8",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Commanding Aura",
            game_text="As long as Hariyama ex is your Active Pok\u00e9mon, your opponent can't play any Stadium cards from his or her hand.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=commanding_aura_no_stadium(),
        ),
        Attack(
            title="Knock Off",
            game_text="Choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=knock_off_random_hand(),
        ),
        Attack(
            title="Pivot Throw",
            game_text="During your opponent's next turn, any damage done to Hariyama ex by attacks is increased by 10 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=pivot_throw_takes_more(),
        ),
    ],
)