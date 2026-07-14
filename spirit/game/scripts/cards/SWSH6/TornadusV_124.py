from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, self_energy_discard_attack

card = PokemonCardDef(
    guid="ea22f75d-ce7a-59fd-8b96-ea0ec61589dc",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusV.Name",
    display_name="Tornadus V",
    searchable_by=["Tornadus V", "Basic", "V", "Single Strike", "TornadusV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=124,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If a Stadium is in play, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 20),
        ),
        Attack(
            title="Blasting Hammer",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            effect=self_energy_discard_attack(count=1, before_damage=True),
        ),
    ],
)