from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class SelfishLipsPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier or not ctx.is_attack_effect():
            return count
        attacker = getattr(ctx, "attacker", None)
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return count
        if is_pokemon_v(attacker.archetype_id):
            return 0
        return count


card = PokemonCardDef(
    guid="b8036ff5-5469-5c03-b35d-8af455498be8",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=124,
    abilities=[
        Ability(
            title="Selfish Lips",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon V, your opponent can't take any Prize cards for it.",
            passive=SelfishLipsPassive(),
        ),
        Attack(
            title="Psychic Assault",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=10),
        ),
    ],
)
