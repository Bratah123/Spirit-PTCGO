from spirit.game.card_effects.ex import dark_spell_snipe, hide_in_shadows
"""STUB: effect not implemented — do not guess mechanics.
Misdreavus (EX7 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3e531898-4a74-5e2e-bd24-1cb2c0f72d5a",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic", "Misdreavus"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX7",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=200,
    abilities=[
        Ability(
            title="Dark Spell",
            game_text="Once during your turn (before your attack), if Misdreavus is your Active Pok\u00e9mon, you may flip a coin. If heads, put 1 damage counter on 1 of your opponent's Pok\u00e9mon. This power can't be used if Misdreavus is affected by a Special Condition or if your other Active Pok\u00e9mon is not Misdreavus.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=dark_spell_snipe(),
        ),
        Attack(
            title="Hide in Shadows",
            game_text="Switch Misdreavus with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=hide_in_shadows(),
        ),
    ],
)