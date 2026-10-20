from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack, bonus_if


card = PokemonCardDef(
    guid="70a365cd-3855-50bd-b1d7-1c837d562677",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic", "Stunfisk"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=618,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.kos_suffered_last_turn() > 0, 80),
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)