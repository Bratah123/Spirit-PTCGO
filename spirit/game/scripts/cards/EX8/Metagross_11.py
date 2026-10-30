"""STUB: effect not implemented — do not guess mechanics.
Metagross (EX8 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import link_blast, super_connectivity_attach


card = PokemonCardDef(
    guid="a21c8d8d-c984-5940-a49b-184ac54badb8",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Super Connectivity",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Psychic or Metal Energy card and attach it to your Active Pok\u00e9mon. Then, put 1 damage counter on that Pok\u00e9mon. This power can't be used if Metagross is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=super_connectivity_attach(),
        ),
        Attack(
            title="Link Blast",
            game_text="If Metagross and the Defending Pok\u00e9mon have a different amount of Energy attached to them, this attack's base damage is 40 instead of 70.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=link_blast(70, 40),
        ),
    ],
)