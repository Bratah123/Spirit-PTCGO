"""STUB: effect not implemented — do not guess mechanics.
Nidoqueen δ (EX15 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import invitation_search_pokemon, vengeance


card = PokemonCardDef(
    guid="a8c65854-b5e8-599e-a04b-0f67f288ae19",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen δ",
    searchable_by=["Nidoqueen \u03b4", "Stage 2", "Nidoqueen"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=31,
    abilities=[
        Ability(
            title="Invitation",
            game_text="Once during your turn (before your attack), you may search your deck for a Basic Pok\u00e9mon or Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Nidoqueen is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=invitation_search_pokemon(),
        ),
        Attack(
            title="Vengeance",
            game_text="Does 30 damage plus 10 more damage for each Basic Pok\u00e9mon and each Evolution card in your discard pile. You can't add more than 60 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=vengeance(30, 10),
        ),
    ],
)