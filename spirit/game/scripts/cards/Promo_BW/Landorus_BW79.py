from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack, bonus_if


card = PokemonCardDef(
    guid="1050987c-0559-5708-8451-817f87eb27b9",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic", "Team Plasma", "Landorus"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=79,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=645,
    abilities=[
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)), 30),
        ),
        Attack(
            title="Rock Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)