from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.passives_common import is_in_active_spot, opposing_active
from spirit.game.session.passives import Passive


class IntimidatingFangPassive(Passive):
    def modify_damage_dealt(self, calc, carrier):
        if not is_in_active_spot(carrier):
            return
        attacker = calc.attacker
        if attacker is None or not opposing_active(attacker, carrier):
            return
        calc.amount = max(0, calc.amount - 30)

card = PokemonCardDef(
    guid="cb599bc2-319e-5fab-98f4-f7456439d764",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Intimidating Fang",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon's attacks do 30 less damage (before applying Weakness and Resistance).",
            passive=IntimidatingFangPassive(),
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=flip_bonus(100),
        ),
    ],
)