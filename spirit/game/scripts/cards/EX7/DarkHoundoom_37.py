from spirit.game.card_effects.ex import fire_breath_burn_active, fire_payback
"""STUB: effect not implemented — do not guess mechanics.
Dark Houndoom (EX7 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="132c9f9f-86df-55df-b247-7ff5b3ada6df",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkHoundoom.Name",
    display_name="Dark Houndoom",
    searchable_by=["Dark Houndoom", "Stage 1", "DarkHoundoom"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Ability(
            title="Fire Breath",
            game_text="Once during your turn (before your attack), if Dark Houndoom is your Active Pok\u00e9mon, you may flip a coin. If heads, the Defending Pok\u00e9mon (choose 1 if there are 2) is now Burned. This power can't be used if Dark Houndoom is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=fire_breath_burn_active(),
        ),
        Attack(
            title="Fire Payback",
            game_text="If you have less Benched Pok\u00e9mon than your opponent, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=fire_payback(),
        ),
    ],
)