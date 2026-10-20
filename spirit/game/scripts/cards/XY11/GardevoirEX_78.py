from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, bonus_if, count_energy


def _same_energy(ctx):
    d = ctx.opponent_active()
    return d is not None and count_energy('self')(ctx) == count_energy('defender')(ctx)


card = PokemonCardDef(
    guid="4bf10b93-80e9-5547-a32e-c612f681a46a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    display_name="Gardevoir-EX",
    searchable_by=["Gardevoir-EX", "Basic", "EX", "GardevoirEX"],
    subtypes=["Basic", "EX"],
    collector_number=78,
    set_code="XY11",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title="Link Blast",
            game_text="If this Pok\u00e9mon and your opponent's Active Pok\u00e9mon have the same amount of Energy attached to them, this attack does 70 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(_same_energy, 70),
        ),
        Attack(
            title="Luminous Blade",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)