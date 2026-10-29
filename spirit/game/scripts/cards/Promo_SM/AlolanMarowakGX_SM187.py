from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.smp import cursed_body, lost_boomerang_gx


card = PokemonCardDef(
    guid="a1cfff77-c983-535d-a7c0-adc034013271",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowakGX.Name",
    display_name="Alolan Marowak-GX",
    searchable_by=["Alolan Marowak-GX", "Stage 1", "GX", "AlolanMarowakGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=187,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=105,
    abilities=[
        Ability(
            title="Cursed Body",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Confused.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=cursed_body,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Fiery Bone",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Lost Boomerang-GX",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness or Resistance. If a Pok\u00e9mon is Knocked Out by this damage, put that Pok\u00e9mon and all cards attached to it in the Lost Zone instead of the discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=lost_boomerang_gx,
        ),
    ],
)