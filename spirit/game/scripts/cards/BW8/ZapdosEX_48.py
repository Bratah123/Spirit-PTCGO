from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.effects import plasma_energy_attached


card = PokemonCardDef(
    guid="84bf6828-6a14-513b-9a6e-f2576cdaa22a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZapdosEX.Name",
    display_name="Zapdos-EX",
    searchable_by=["Zapdos-EX", "Basic", "EX", "Team Plasma", "ZapdosEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=48,
    set_code="BW8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=145,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Powervolt",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(lambda ctx: bool(plasma_energy_attached(ctx.attacker)), 40),
        ),
    ],
)