from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.ecard import has_fire_energy_attached, opponent_has_benched
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="c70a5f78-53dd-593c-b295-24cf7cbf2207",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Lure",
            game_text="If your opponent has any Benched Pokémon, choose 1 of them and switch it with the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            condition=opponent_has_benched,
            effect=gust_attack(),
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard 1 Fire Energy card attached to Ninetales in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=80,
            condition=has_fire_energy_attached,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.FIRE),
        ),
    ],
)
