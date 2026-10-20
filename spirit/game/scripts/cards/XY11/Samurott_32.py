"""STUB: effect not implemented — do not guess mechanics.
Samurott (XY11 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="d67ed84e-dc0f-5bce-94bb-685a880b3964",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Samurott.Name",
    display_name="Samurott",
    searchable_by=["Samurott", "Stage 2", "Samurott"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    family_id=501,
    abilities=[
        Attack(
            title="Ultimate Blade",
            game_text="If the damage from this attack reduces your opponent's Active Pok\u00e9mon's HP to 60 or less, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pike",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            # STUB: attack effect not implemented
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)