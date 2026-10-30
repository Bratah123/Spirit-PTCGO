from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.ecard import guiding_flame, has_typed_basic_energy


card = PokemonCardDef(
    guid="7f2bc2c8-ecae-56ca-a686-d67e77430077",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightNinetales.Name",
    display_name="Light Ninetales",
    searchable_by=["Light Ninetales", "Stage 1", "LightNinetales"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Guiding Flame",
            game_text="Put a Baby Pok\u00e9mon or a Basic Pok\u00e9mon card from your discard pile onto your Bench. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.FIRE: 1},
            condition=requires_bench_space(),
            effect=guiding_flame,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy card attached to Light Ninetales in order to use this attack.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            condition=has_typed_basic_energy(PokemonTypes.FIRE),
            effect=self_energy_discard_attack(
                count=1, energy_type=PokemonTypes.FIRE, before_damage=True),
        ),
    ],
)
