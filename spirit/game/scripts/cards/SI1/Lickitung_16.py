from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, snipe_attack
from spirit.game.card_effects.ecard import lick_wounds


card = PokemonCardDef(
    guid="0738d786-1cc8-53a4-ad40-51606c731d8c",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=108,
    abilities=[
        Attack(
            title="Lick Wounds",
            game_text="Flip a coin. If heads, choose 1 Pok\u00e9mon (yours or your opponent's) with damage counters on it and remove 2 damage counters from it (1 if it only has 1).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lick_wounds,
        ),
        Attack(
            title="Tongue Stretch",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=flip_or_nothing(then=snipe_attack(
                20, pool="any", apply_modifiers=False)),
        ),
    ],
)
