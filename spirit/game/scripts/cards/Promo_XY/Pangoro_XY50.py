from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.attacks_common import bonus_if


class _BenevolentBoss(Passive):
    """While this Pokemon is Active it gets +20 HP per Benched Pokemon you have."""
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier or not is_in_active_spot(pokemon):
            return 0
        player_area = pokemon.parent.parent if pokemon.parent is not None else None
        for area in (player_area.children if player_area is not None else []):
            if area.get_attribute(AttrID.NAME) == "bench":
                return 20 * sum(1 for c in area.children if is_pokemon_card(c))
        return 0


def _self_conditioned(ctx):
    return bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="bcff5285-5bf5-58ff-811c-ecc1b0c9719e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pangoro.Name",
    display_name="Pangoro",
    searchable_by=["Pangoro", "Stage 1", "Pangoro"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    family_id=675,
    abilities=[
        Ability(
            title="Benevolent Boss",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, it gets +20 HP for each of your Benched Pok\u00e9mon.",
            passive=_BenevolentBoss(),
        ),
        Attack(
            title="Crazy Knuckle",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(_self_conditioned, 40),
        ),
    ],
)