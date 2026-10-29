from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.smp import dusk_shot, rusty_claws

card = PokemonCardDef(
    guid="6fc7dbc3-c3f5-59fe-9f83-dd6686596065",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozma.Name",
    display_name="Dusk Mane Necrozma",
    searchable_by=["Dusk Mane Necrozma", "Basic", "Ultra Beast", "DuskManeNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=107,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Attack(
            title="Dusk Shot",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.METAL: 1},
            effect=dusk_shot,
        ),
        Attack(
            title="Rusty Claws",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 100 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=rusty_claws,
        ),
    ],
)