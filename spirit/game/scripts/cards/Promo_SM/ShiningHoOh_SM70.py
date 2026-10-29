from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.smp import golden_wing


card = PokemonCardDef(
    guid="e05a32cd-0060-560b-a9c1-81b8f736b66c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningHoOh.Name",
    display_name="Shining Ho-Oh",
    searchable_by=["Shining Ho-Oh", "Basic", "ShiningHoOh"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Wing",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, move up to 2 basic Energy cards from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=golden_wing,
            trigger=Triggers.ON_KNOCKED_OUT,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)