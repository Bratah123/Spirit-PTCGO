"""STUB: effect not implemented — do not guess mechanics.
Murkrow (POP1 #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import feint_attack, insomnia_passive


card = PokemonCardDef(
    guid="7f13afd1-9dd0-578b-bf7b-250559f0912e",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="POP1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Ability(
            title="Insomnia",
            game_text="Murkrow can't be Asleep.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=insomnia_passive(),
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on that Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=feint_attack(20),
        ),
    ],
)